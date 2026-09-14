# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T00:07:27.428501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.313` n `233`; crypto_major avg `0.2465` n `8`; equity avg `0.3343` n `136`; fx avg `0.0328` n `6`; index avg `-0.0314` n `27`; metal avg `0.1105` n `20`; unknown avg `2.8966` n `838`
- 1h: commodity avg `0.0107` n `12`; crypto_alt avg `0.4036` n `233`; crypto_major avg `0.2308` n `8`; equity avg `0.0335` n `136`; fx avg `0.0241` n `6`; index avg `-0.1255` n `27`; metal avg `0.0251` n `20`; unknown avg `4.3763` n `818`
- 4h: commodity avg `0.3089` n `12`; crypto_alt avg `-1.3054` n `233`; crypto_major avg `-0.8083` n `8`; equity avg `-0.2842` n `136`; fx avg `0.0563` n `6`; index avg `-0.1636` n `27`; metal avg `-0.0178` n `20`; unknown avg `23.6063` n `782`
- 24h: commodity avg `0.6598` n `12`; crypto_alt avg `-1.4025` n `233`; crypto_major avg `-1.4725` n `8`; equity avg `-1.4614` n `136`; fx avg `0.0733` n `6`; index avg `-0.4093` n `26`; metal avg `-0.0766` n `20`; unknown avg `1.6173` n `696`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
