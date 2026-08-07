# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T09:52:32.694560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.0119` n `230`; crypto_major avg `-0.0413` n `8`; equity avg `-0.0` n `112`; fx avg `-0.0082` n `6`; index avg `-0.0036` n `25`; metal avg `0.0773` n `20`; unknown avg `0.1608` n `782`
- 1h: commodity avg `-0.1824` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `0.3855` n `8`; equity avg `0.0929` n `112`; fx avg `-0.0208` n `6`; index avg `0.0165` n `25`; metal avg `0.092` n `20`; unknown avg `0.1095` n `782`
- 4h: commodity avg `-0.2334` n `12`; crypto_alt avg `0.0613` n `230`; crypto_major avg `0.9202` n `8`; equity avg `0.8088` n `112`; fx avg `-0.0449` n `6`; index avg `0.1091` n `25`; metal avg `0.4152` n `20`; unknown avg `0.2235` n `766`
- 24h: commodity avg `0.3539` n `12`; crypto_alt avg `0.6302` n `230`; crypto_major avg `0.2406` n `8`; equity avg `2.0125` n `109`; fx avg `-0.0883` n `6`; index avg `0.0549` n `25`; metal avg `0.3766` n `20`; unknown avg `43.5405` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
