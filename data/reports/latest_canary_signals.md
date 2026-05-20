# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T10:52:18.101122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1001` n `12`; crypto_alt avg `-0.1459` n `228`; crypto_major avg `-0.0875` n `8`; equity avg `-0.054` n `66`; fx avg `0.0011` n `6`; index avg `-0.0471` n `23`; metal avg `-0.0272` n `18`; unknown avg `-0.2053` n `384`
- 1h: commodity avg `-0.3721` n `12`; crypto_alt avg `0.0646` n `228`; crypto_major avg `0.2397` n `8`; equity avg `0.0833` n `66`; fx avg `0.0003` n `6`; index avg `-0.0875` n `23`; metal avg `0.106` n `18`; unknown avg `0.3346` n `384`
- 4h: commodity avg `-0.5055` n `12`; crypto_alt avg `0.0879` n `228`; crypto_major avg `0.2853` n `8`; equity avg `0.5059` n `66`; fx avg `-0.0214` n `6`; index avg `0.2392` n `23`; metal avg `0.276` n `18`; unknown avg `-0.097` n `384`
- 24h: commodity avg `-0.5436` n `12`; crypto_alt avg `0.8936` n `228`; crypto_major avg `0.7087` n `8`; equity avg `1.498` n `66`; fx avg `-0.1542` n `6`; index avg `0.2043` n `23`; metal avg `-0.577` n `18`; unknown avg `0.4328` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0476`, n `668`, weak_sample_signal
