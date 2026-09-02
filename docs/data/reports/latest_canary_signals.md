# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T05:07:47.684696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0557` n `12`; crypto_alt avg `-0.1868` n `232`; crypto_major avg `-0.1689` n `8`; equity avg `-0.0563` n `132`; fx avg `-0.0056` n `6`; index avg `-0.0111` n `26`; metal avg `0.0165` n `20`; unknown avg `-0.1165` n `790`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `0.1015` n `232`; crypto_major avg `0.0026` n `8`; equity avg `-0.0118` n `132`; fx avg `-0.0361` n `6`; index avg `-0.0097` n `26`; metal avg `0.0365` n `20`; unknown avg `1.3728` n `790`
- 4h: commodity avg `-0.1632` n `12`; crypto_alt avg `0.8012` n `232`; crypto_major avg `0.2609` n `8`; equity avg `-0.3256` n `132`; fx avg `-0.0778` n `6`; index avg `-0.0985` n `26`; metal avg `-0.0745` n `20`; unknown avg `2.7862` n `790`
- 24h: commodity avg `0.7638` n `12`; crypto_alt avg `-0.817` n `232`; crypto_major avg `-1.9571` n `8`; equity avg `-2.5734` n `130`; fx avg `-0.1015` n `6`; index avg `-0.4608` n `26`; metal avg `-1.0365` n `20`; unknown avg `-0.4407` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0415`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0412`, n `668`, weak_sample_signal
