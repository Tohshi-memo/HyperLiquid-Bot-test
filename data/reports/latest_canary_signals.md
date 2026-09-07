# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T16:22:32.183267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2731` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0759` n `12`; crypto_alt avg `0.092` n `232`; crypto_major avg `0.0374` n `8`; equity avg `0.0573` n `134`; fx avg `-0.0007` n `6`; index avg `0.0135` n `26`; metal avg `0.0034` n `20`; unknown avg `0.9066` n `796`
- 1h: commodity avg `-0.0714` n `12`; crypto_alt avg `-0.6868` n `232`; crypto_major avg `-0.5234` n `8`; equity avg `-0.0621` n `134`; fx avg `-0.0033` n `6`; index avg `0.0268` n `26`; metal avg `0.012` n `20`; unknown avg `0.0085` n `794`
- 4h: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.9716` n `232`; crypto_major avg `-1.2208` n `8`; equity avg `-0.0544` n `134`; fx avg `-0.049` n `6`; index avg `0.0523` n `26`; metal avg `0.1962` n `20`; unknown avg `-0.3346` n `788`
- 24h: commodity avg `0.1213` n `12`; crypto_alt avg `-0.1572` n `232`; crypto_major avg `-1.143` n `8`; equity avg `0.3633` n `134`; fx avg `-0.1193` n `6`; index avg `0.06` n `26`; metal avg `0.0289` n `20`; unknown avg `146.7328` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
