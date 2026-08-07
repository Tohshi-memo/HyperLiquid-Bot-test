# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T03:07:26.250433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.0679` n `230`; crypto_major avg `-0.0164` n `8`; equity avg `0.0415` n `112`; fx avg `0.0103` n `6`; index avg `0.0259` n `25`; metal avg `0.0248` n `20`; unknown avg `-0.2343` n `782`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.0864` n `230`; crypto_major avg `-0.0656` n `8`; equity avg `0.2953` n `112`; fx avg `0.0112` n `6`; index avg `0.0259` n `25`; metal avg `-0.0605` n `20`; unknown avg `0.5132` n `782`
- 4h: commodity avg `-0.0417` n `12`; crypto_alt avg `0.2038` n `230`; crypto_major avg `-0.0856` n `8`; equity avg `0.2412` n `112`; fx avg `-0.031` n `6`; index avg `-0.1008` n `25`; metal avg `0.1345` n `20`; unknown avg `-0.0254` n `782`
- 24h: commodity avg `0.4856` n `12`; crypto_alt avg `0.7047` n `230`; crypto_major avg `-0.4317` n `8`; equity avg `0.8372` n `109`; fx avg `0.039` n `6`; index avg `-0.1201` n `25`; metal avg `-0.1366` n `20`; unknown avg `113.2557` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
