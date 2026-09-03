# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T02:37:27.525981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `0.2619` n `232`; crypto_major avg `0.3436` n `8`; equity avg `-0.0237` n `133`; fx avg `-0.0057` n `6`; index avg `-0.0001` n `26`; metal avg `0.0119` n `20`; unknown avg `0.6014` n `792`
- 1h: commodity avg `0.0559` n `12`; crypto_alt avg `0.2942` n `232`; crypto_major avg `0.524` n `8`; equity avg `0.0289` n `133`; fx avg `-0.0208` n `6`; index avg `-0.0049` n `26`; metal avg `0.0349` n `20`; unknown avg `0.6653` n `790`
- 4h: commodity avg `0.1021` n `12`; crypto_alt avg `1.0638` n `232`; crypto_major avg `1.0496` n `8`; equity avg `0.1122` n `133`; fx avg `-0.0681` n `6`; index avg `-0.0213` n `26`; metal avg `0.1406` n `20`; unknown avg `0.605` n `790`
- 24h: commodity avg `0.2202` n `12`; crypto_alt avg `0.6447` n `232`; crypto_major avg `0.7668` n `8`; equity avg `1.3475` n `133`; fx avg `-0.3847` n `6`; index avg `0.1433` n `26`; metal avg `0.7718` n `20`; unknown avg `-0.2031` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
