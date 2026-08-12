# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T06:03:03.193095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `-0.0353` n `230`; crypto_major avg `-0.0553` n `8`; equity avg `0.2427` n `113`; fx avg `-0.0029` n `6`; index avg `0.0028` n `25`; metal avg `0.0234` n `20`; unknown avg `0.0033` n `770`
- 1h: commodity avg `0.0437` n `12`; crypto_alt avg `-0.0689` n `230`; crypto_major avg `0.0604` n `8`; equity avg `0.1861` n `113`; fx avg `-0.0006` n `6`; index avg `0.0232` n `25`; metal avg `-0.0674` n `20`; unknown avg `-0.007` n `770`
- 4h: commodity avg `0.0717` n `12`; crypto_alt avg `-0.2423` n `230`; crypto_major avg `-0.2908` n `8`; equity avg `0.5687` n `113`; fx avg `0.0003` n `6`; index avg `0.0898` n `25`; metal avg `0.0364` n `20`; unknown avg `-0.0174` n `770`
- 24h: commodity avg `0.2442` n `12`; crypto_alt avg `-1.0286` n `230`; crypto_major avg `0.6945` n `8`; equity avg `1.9888` n `113`; fx avg `0.0015` n `6`; index avg `0.156` n `25`; metal avg `0.0254` n `20`; unknown avg `-0.059` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2248`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2173`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
