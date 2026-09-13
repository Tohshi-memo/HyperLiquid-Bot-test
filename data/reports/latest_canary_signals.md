# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T23:52:28.350865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.0198` n `233`; crypto_major avg `-0.0287` n `8`; equity avg `-0.183` n `136`; fx avg `0.0008` n `6`; index avg `-0.0715` n `27`; metal avg `-0.0651` n `20`; unknown avg `0.9553` n `820`
- 1h: commodity avg `0.0237` n `12`; crypto_alt avg `0.0702` n `233`; crypto_major avg `-0.0722` n `8`; equity avg `-0.3044` n `136`; fx avg `-0.0253` n `6`; index avg `-0.0817` n `27`; metal avg `-0.0502` n `20`; unknown avg `2.4713` n `818`
- 4h: commodity avg `0.3109` n `12`; crypto_alt avg `-1.4588` n `233`; crypto_major avg `-0.8976` n `8`; equity avg `-0.6101` n `136`; fx avg `0.0304` n `6`; index avg `-0.119` n `27`; metal avg `-0.1228` n `20`; unknown avg `18.0372` n `782`
- 24h: commodity avg `0.6516` n `12`; crypto_alt avg `-1.6834` n `233`; crypto_major avg `-1.7804` n `8`; equity avg `-1.7914` n `136`; fx avg `0.0421` n `6`; index avg `-0.3801` n `26`; metal avg `-0.1798` n `20`; unknown avg `1.3735` n `696`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
