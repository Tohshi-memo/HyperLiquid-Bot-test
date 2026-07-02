# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T15:37:34.622453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.1794` n `229`; crypto_major avg `0.233` n `8`; equity avg `0.6261` n `88`; fx avg `-0.0329` n `6`; index avg `0.1219` n `25`; metal avg `0.1189` n `20`; unknown avg `-0.0243` n `763`
- 1h: commodity avg `0.0304` n `12`; crypto_alt avg `-0.2058` n `229`; crypto_major avg `-0.0763` n `8`; equity avg `-0.8145` n `88`; fx avg `-0.0678` n `6`; index avg `-0.1257` n `25`; metal avg `0.1026` n `20`; unknown avg `0.0526` n `763`
- 4h: commodity avg `0.1843` n `12`; crypto_alt avg `-0.0418` n `229`; crypto_major avg `0.6208` n `8`; equity avg `-0.6075` n `88`; fx avg `-0.0505` n `6`; index avg `-0.0672` n `25`; metal avg `0.6768` n `20`; unknown avg `-0.2011` n `763`
- 24h: commodity avg `-0.2439` n `12`; crypto_alt avg `1.2621` n `228`; crypto_major avg `2.5226` n `8`; equity avg `-2.2982` n `88`; fx avg `-0.0769` n `6`; index avg `-0.4882` n `25`; metal avg `0.763` n `20`; unknown avg `1.4118` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
