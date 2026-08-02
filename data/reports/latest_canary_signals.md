# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T14:37:25.146523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `0.1425` n `230`; crypto_major avg `0.0797` n `8`; equity avg `0.0344` n `102`; fx avg `0.0199` n `6`; index avg `0.0239` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0337` n `782`
- 1h: commodity avg `-0.1095` n `12`; crypto_alt avg `0.2124` n `230`; crypto_major avg `0.202` n `8`; equity avg `0.0117` n `102`; fx avg `-0.0266` n `6`; index avg `0.0126` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.0634` n `782`
- 4h: commodity avg `-0.0633` n `12`; crypto_alt avg `0.0045` n `230`; crypto_major avg `-0.0008` n `8`; equity avg `-0.2071` n `102`; fx avg `-0.0503` n `6`; index avg `-0.0243` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0893` n `782`
- 24h: commodity avg `-1.0892` n `12`; crypto_alt avg `0.2401` n `230`; crypto_major avg `0.1119` n `8`; equity avg `0.8665` n `102`; fx avg `-0.1457` n `6`; index avg `0.1998` n `25`; metal avg `0.2473` n `20`; unknown avg `0.236` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
