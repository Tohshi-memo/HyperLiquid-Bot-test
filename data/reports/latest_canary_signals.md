# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T08:52:25.198165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `0.0223` n `230`; crypto_major avg `0.1559` n `8`; equity avg `-0.0046` n `112`; fx avg `0.0067` n `6`; index avg `0.0093` n `25`; metal avg `-0.0154` n `20`; unknown avg `0.002` n `782`
- 1h: commodity avg `-0.0345` n `12`; crypto_alt avg `0.0841` n `230`; crypto_major avg `0.3142` n `8`; equity avg `0.46` n `112`; fx avg `-0.0166` n `6`; index avg `0.0359` n `25`; metal avg `0.1628` n `20`; unknown avg `0.0608` n `782`
- 4h: commodity avg `-0.0576` n `12`; crypto_alt avg `0.5827` n `230`; crypto_major avg `0.6644` n `8`; equity avg `1.1294` n `112`; fx avg `-0.0278` n `6`; index avg `0.1453` n `25`; metal avg `0.4583` n `20`; unknown avg `0.0685` n `766`
- 24h: commodity avg `0.6343` n `12`; crypto_alt avg `0.1968` n `230`; crypto_major avg `-0.7832` n `8`; equity avg `1.8504` n `109`; fx avg `-0.0783` n `6`; index avg `0.0212` n `25`; metal avg `0.3289` n `20`; unknown avg `110.801` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
