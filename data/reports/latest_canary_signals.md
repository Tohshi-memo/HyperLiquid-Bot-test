# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T09:52:31.051055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `0.0823` n `233`; crypto_major avg `0.1512` n `8`; equity avg `0.2313` n `136`; fx avg `-0.0056` n `6`; index avg `0.047` n `27`; metal avg `0.0419` n `20`; unknown avg `0.5172` n `908`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `0.2024` n `233`; crypto_major avg `0.3531` n `8`; equity avg `0.3134` n `136`; fx avg `-0.017` n `6`; index avg `0.074` n `27`; metal avg `0.0728` n `20`; unknown avg `1.2333` n `906`
- 4h: commodity avg `0.177` n `12`; crypto_alt avg `-0.4746` n `233`; crypto_major avg `-0.4114` n `8`; equity avg `-0.1683` n `136`; fx avg `0.0794` n `6`; index avg `-0.0441` n `27`; metal avg `-0.1952` n `20`; unknown avg `17.0512` n `876`
- 24h: commodity avg `0.0647` n `12`; crypto_alt avg `-1.4737` n `233`; crypto_major avg `-1.0885` n `8`; equity avg `0.1991` n `136`; fx avg `0.2471` n `6`; index avg `0.0397` n `27`; metal avg `0.0101` n `20`; unknown avg `-0.0452` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
