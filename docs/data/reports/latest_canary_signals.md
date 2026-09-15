# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T01:52:30.953317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.044` n `12`; crypto_alt avg `0.0566` n `233`; crypto_major avg `0.0996` n `8`; equity avg `-0.0473` n `136`; fx avg `0.0198` n `6`; index avg `-0.0004` n `27`; metal avg `-0.0216` n `20`; unknown avg `0.2782` n `908`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.0946` n `233`; crypto_major avg `0.0799` n `8`; equity avg `-0.1704` n `136`; fx avg `0.0296` n `6`; index avg `-0.0042` n `27`; metal avg `0.0283` n `20`; unknown avg `-0.19` n `906`
- 4h: commodity avg `0.0893` n `12`; crypto_alt avg `-0.4281` n `233`; crypto_major avg `-0.7211` n `8`; equity avg `0.1378` n `136`; fx avg `0.0391` n `6`; index avg `0.0695` n `27`; metal avg `-0.0592` n `20`; unknown avg `0.5027` n `888`
- 24h: commodity avg `-0.0304` n `12`; crypto_alt avg `0.7999` n `233`; crypto_major avg `2.0163` n `8`; equity avg `0.0971` n `136`; fx avg `0.07` n `6`; index avg `0.0038` n `27`; metal avg `-0.4404` n `20`; unknown avg `5.4464` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
