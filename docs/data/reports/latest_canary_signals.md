# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T21:10:13.744151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `-0.1315` n `228`; crypto_major avg `-0.1399` n `8`; equity avg `0.0217` n `88`; fx avg `-0.0056` n `6`; index avg `0.011` n `23`; metal avg `-0.0287` n `20`; unknown avg `-0.0462` n `765`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.5057` n `228`; crypto_major avg `-0.5057` n `8`; equity avg `0.006` n `88`; fx avg `-0.0236` n `6`; index avg `-0.0397` n `23`; metal avg `-0.1983` n `20`; unknown avg `-0.1737` n `765`
- 4h: commodity avg `-0.0736` n `12`; crypto_alt avg `-0.6194` n `228`; crypto_major avg `-0.1434` n `8`; equity avg `0.2902` n `88`; fx avg `-0.0085` n `6`; index avg `-0.0537` n `23`; metal avg `-0.1872` n `20`; unknown avg `1.0469` n `763`
- 24h: commodity avg `0.1371` n `12`; crypto_alt avg `-2.3136` n `228`; crypto_major avg `-2.2272` n `8`; equity avg `1.1867` n `88`; fx avg `0.13` n `6`; index avg `0.2151` n `23`; metal avg `-0.0675` n `20`; unknown avg `8.1774` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
