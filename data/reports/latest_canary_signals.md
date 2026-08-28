# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T04:22:31.339844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0062` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.2086` n `231`; crypto_major avg `0.1341` n `8`; equity avg `0.0669` n `127`; fx avg `0.0028` n `6`; index avg `0.0232` n `26`; metal avg `0.0513` n `20`; unknown avg `-0.1013` n `792`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `-0.0894` n `231`; crypto_major avg `-0.1753` n `8`; equity avg `-0.1368` n `127`; fx avg `-0.0043` n `6`; index avg `-0.0135` n `26`; metal avg `-0.0004` n `20`; unknown avg `-0.1175` n `792`
- 4h: commodity avg `-0.017` n `12`; crypto_alt avg `-1.4347` n `231`; crypto_major avg `-0.9721` n `8`; equity avg `-0.0404` n `127`; fx avg `-0.0456` n `6`; index avg `0.0341` n `26`; metal avg `-0.025` n `20`; unknown avg `-0.2007` n `792`
- 24h: commodity avg `0.277` n `12`; crypto_alt avg `0.4295` n `231`; crypto_major avg `1.7303` n `8`; equity avg `-0.12` n `127`; fx avg `-0.0278` n `6`; index avg `0.0406` n `26`; metal avg `-0.0465` n `20`; unknown avg `0.5814` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
