# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T21:22:24.973648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `12`; crypto_alt avg `0.0825` n `230`; crypto_major avg `0.0016` n `8`; equity avg `0.0494` n `102`; fx avg `0.0093` n `6`; index avg `0.01` n `25`; metal avg `0.0091` n `20`; unknown avg `0.0164` n `782`
- 1h: commodity avg `-0.0362` n `12`; crypto_alt avg `0.1099` n `230`; crypto_major avg `0.1861` n `8`; equity avg `0.0714` n `102`; fx avg `0.0023` n `6`; index avg `0.0145` n `25`; metal avg `0.0313` n `20`; unknown avg `0.1195` n `782`
- 4h: commodity avg `0.0135` n `12`; crypto_alt avg `-0.6598` n `230`; crypto_major avg `-0.6012` n `8`; equity avg `-0.1461` n `102`; fx avg `0.0037` n `6`; index avg `-0.0338` n `25`; metal avg `0.0325` n `20`; unknown avg `-0.0478` n `782`
- 24h: commodity avg `0.0633` n `12`; crypto_alt avg `-0.5869` n `230`; crypto_major avg `-1.0731` n `8`; equity avg `-0.4565` n `102`; fx avg `-0.0387` n `6`; index avg `-0.0692` n `25`; metal avg `0.0436` n `20`; unknown avg `4.3377` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
