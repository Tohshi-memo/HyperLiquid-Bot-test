# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T05:52:27.055689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0827` n `230`; crypto_major avg `-0.0738` n `8`; equity avg `-0.0692` n `120`; fx avg `0.0257` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.0644` n `789`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `0.0896` n `230`; crypto_major avg `-0.0412` n `8`; equity avg `0.0248` n `120`; fx avg `-0.0157` n `6`; index avg `0.0254` n `25`; metal avg `-0.0291` n `20`; unknown avg `0.1315` n `789`
- 4h: commodity avg `-0.0633` n `12`; crypto_alt avg `-0.1409` n `230`; crypto_major avg `-0.1039` n `8`; equity avg `-0.8653` n `120`; fx avg `-0.0937` n `6`; index avg `-0.1147` n `25`; metal avg `-0.087` n `20`; unknown avg `-0.2792` n `789`
- 24h: commodity avg `0.3678` n `12`; crypto_alt avg `0.6114` n `230`; crypto_major avg `0.2178` n `8`; equity avg `-3.309` n `120`; fx avg `-0.1686` n `6`; index avg `-0.4977` n `25`; metal avg `-0.6624` n `20`; unknown avg `-0.2487` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
