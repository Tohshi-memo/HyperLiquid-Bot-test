# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T10:07:37.994873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0554` n `12`; crypto_alt avg `0.0188` n `230`; crypto_major avg `0.0003` n `8`; equity avg `-0.0837` n `112`; fx avg `-0.0005` n `6`; index avg `-0.0173` n `25`; metal avg `-0.0618` n `20`; unknown avg `-0.0483` n `782`
- 1h: commodity avg `-0.1611` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.2547` n `8`; equity avg `-0.0131` n `112`; fx avg `-0.012` n `6`; index avg `-0.0293` n `25`; metal avg `0.0321` n `20`; unknown avg `0.0606` n `782`
- 4h: commodity avg `-0.2486` n `12`; crypto_alt avg `0.0146` n `230`; crypto_major avg `0.838` n `8`; equity avg `0.667` n `112`; fx avg `-0.0683` n `6`; index avg `0.07` n `25`; metal avg `0.2804` n `20`; unknown avg `0.2192` n `782`
- 24h: commodity avg `0.3472` n `12`; crypto_alt avg `0.7513` n `230`; crypto_major avg `0.3198` n `8`; equity avg `1.8269` n `109`; fx avg `-0.0848` n `6`; index avg `0.0199` n `25`; metal avg `0.3282` n `20`; unknown avg `0.423` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
