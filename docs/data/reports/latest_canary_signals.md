# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T06:37:30.815154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `0.3414` n `236`; crypto_major avg `0.3478` n `8`; equity avg `-0.0314` n `151`; fx avg `-0.0516` n `6`; index avg `-0.0361` n `26`; metal avg `0.0021` n `20`; unknown avg `-0.0647` n `1136`
- 1h: commodity avg `-0.0329` n `13`; crypto_alt avg `-0.0046` n `236`; crypto_major avg `0.0945` n `8`; equity avg `-0.0366` n `151`; fx avg `-0.0937` n `6`; index avg `0.0261` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.001` n `1108`
- 4h: commodity avg `-0.0283` n `13`; crypto_alt avg `-0.367` n `236`; crypto_major avg `-0.1827` n `8`; equity avg `-0.2411` n `151`; fx avg `-0.0887` n `6`; index avg `-0.004` n `26`; metal avg `-0.0417` n `20`; unknown avg `0.8998` n `1102`
- 24h: commodity avg `-0.3728` n `13`; crypto_alt avg `-5.2082` n `236`; crypto_major avg `-3.5685` n `8`; equity avg `-5.7319` n `151`; fx avg `0.0014` n `6`; index avg `-0.928` n `26`; metal avg `-0.7227` n `20`; unknown avg `1392.7113` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0971`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.068`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0588`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
