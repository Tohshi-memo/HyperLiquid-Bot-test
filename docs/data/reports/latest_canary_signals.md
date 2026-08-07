# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T00:22:24.024651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `-0.1296` n `230`; crypto_major avg `-0.2316` n `8`; equity avg `-0.5096` n `112`; fx avg `-0.0112` n `6`; index avg `-0.1257` n `25`; metal avg `-0.0566` n `20`; unknown avg `0.4727` n `782`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `0.2089` n `230`; crypto_major avg `0.0653` n `8`; equity avg `-0.3553` n `112`; fx avg `0.0064` n `6`; index avg `-0.0715` n `25`; metal avg `-0.0359` n `20`; unknown avg `-0.1324` n `782`
- 4h: commodity avg `0.1237` n `12`; crypto_alt avg `0.1659` n `230`; crypto_major avg `-0.1696` n `8`; equity avg `0.1847` n `112`; fx avg `-0.0031` n `6`; index avg `-0.0494` n `25`; metal avg `-0.0436` n `20`; unknown avg `-0.17` n `782`
- 24h: commodity avg `0.7349` n `12`; crypto_alt avg `0.0817` n `230`; crypto_major avg `-1.3286` n `8`; equity avg `0.3795` n `109`; fx avg `0.0213` n `6`; index avg `-0.1721` n `25`; metal avg `-0.2519` n `20`; unknown avg `112.7372` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
