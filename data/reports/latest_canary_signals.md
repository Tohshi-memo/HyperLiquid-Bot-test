# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T14:37:31.712563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.22` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7407` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0838` n `12`; crypto_alt avg `-0.0906` n `230`; crypto_major avg `-0.0386` n `8`; equity avg `0.0482` n `113`; fx avg `0.0013` n `6`; index avg `0.0287` n `25`; metal avg `-0.0502` n `20`; unknown avg `0.0161` n `786`
- 1h: commodity avg `0.0938` n `12`; crypto_alt avg `-0.541` n `230`; crypto_major avg `-0.4029` n `8`; equity avg `0.3665` n `113`; fx avg `0.0105` n `6`; index avg `0.0489` n `25`; metal avg `0.0598` n `20`; unknown avg `0.0936` n `786`
- 4h: commodity avg `0.0448` n `12`; crypto_alt avg `-0.3863` n `230`; crypto_major avg `-0.7322` n `8`; equity avg `1.0085` n `113`; fx avg `0.0044` n `6`; index avg `0.1466` n `25`; metal avg `-0.0305` n `20`; unknown avg `0.0254` n `786`
- 24h: commodity avg `0.2287` n `12`; crypto_alt avg `-1.1818` n `230`; crypto_major avg `0.4207` n `8`; equity avg `2.9582` n `113`; fx avg `0.0428` n `6`; index avg `0.3347` n `25`; metal avg `0.2557` n `20`; unknown avg `-0.0792` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2304`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
