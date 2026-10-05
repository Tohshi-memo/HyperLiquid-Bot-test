# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T03:07:24.580528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.81` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0247` n `13`; crypto_alt avg `-0.2164` n `235`; crypto_major avg `-0.1016` n `8`; equity avg `-0.1506` n `144`; fx avg `-0.0607` n `6`; index avg `-0.0347` n `26`; metal avg `-0.0626` n `20`; unknown avg `0.0931` n `1076`
- 1h: commodity avg `0.0092` n `13`; crypto_alt avg `-0.0501` n `235`; crypto_major avg `-0.1291` n `8`; equity avg `-0.229` n `144`; fx avg `-0.0891` n `6`; index avg `-0.0656` n `26`; metal avg `-0.1715` n `20`; unknown avg `0.2603` n `1076`
- 4h: commodity avg `-0.1465` n `13`; crypto_alt avg `0.4038` n `235`; crypto_major avg `0.0606` n `8`; equity avg `0.0146` n `144`; fx avg `-0.1384` n `6`; index avg `-0.039` n `26`; metal avg `-0.0169` n `20`; unknown avg `4.0732` n `1038`
- 24h: commodity avg `-0.3311` n `13`; crypto_alt avg `1.4718` n `235`; crypto_major avg `1.6692` n `8`; equity avg `0.3451` n `144`; fx avg `-0.1199` n `6`; index avg `-0.0269` n `26`; metal avg `0.0376` n `20`; unknown avg `0.8336` n `950`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
