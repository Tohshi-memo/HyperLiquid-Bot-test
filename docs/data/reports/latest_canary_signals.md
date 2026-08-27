# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T03:37:26.627012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.0052` n `231`; crypto_major avg `-0.0247` n `8`; equity avg `-0.0567` n `126`; fx avg `-0.0095` n `6`; index avg `0.002` n `25`; metal avg `-0.0298` n `20`; unknown avg `-0.0608` n `793`
- 1h: commodity avg `0.0331` n `12`; crypto_alt avg `0.1905` n `231`; crypto_major avg `0.111` n `8`; equity avg `0.1947` n `126`; fx avg `0.0059` n `6`; index avg `0.0091` n `25`; metal avg `0.0555` n `20`; unknown avg `0.3085` n `793`
- 4h: commodity avg `0.0468` n `12`; crypto_alt avg `-0.4143` n `231`; crypto_major avg `-0.3037` n `8`; equity avg `-0.1766` n `126`; fx avg `-0.0553` n `6`; index avg `-0.0811` n `25`; metal avg `0.0908` n `20`; unknown avg `0.298` n `793`
- 24h: commodity avg `0.5095` n `12`; crypto_alt avg `0.4036` n `231`; crypto_major avg `0.5252` n `8`; equity avg `1.3768` n `126`; fx avg `-0.1103` n `6`; index avg `0.1999` n `25`; metal avg `-0.2248` n `20`; unknown avg `0.4715` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
