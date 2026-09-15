# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T08:37:27.080757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0238` n `12`; crypto_alt avg `0.0684` n `233`; crypto_major avg `-0.016` n `8`; equity avg `-0.033` n `136`; fx avg `0.0027` n `6`; index avg `-0.0159` n `27`; metal avg `0.0098` n `20`; unknown avg `0.6114` n `902`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `-0.311` n `233`; crypto_major avg `-0.2967` n `8`; equity avg `-0.3159` n `136`; fx avg `0.0372` n `6`; index avg `-0.0473` n `27`; metal avg `-0.0997` n `20`; unknown avg `17.9339` n `900`
- 4h: commodity avg `0.1192` n `12`; crypto_alt avg `-0.695` n `233`; crypto_major avg `-0.774` n `8`; equity avg `-0.3749` n `136`; fx avg `0.1223` n `6`; index avg `-0.0799` n `27`; metal avg `-0.2262` n `20`; unknown avg `19.8264` n `876`
- 24h: commodity avg `0.016` n `12`; crypto_alt avg `-1.588` n `233`; crypto_major avg `-1.0672` n `8`; equity avg `-0.2843` n `136`; fx avg `0.2347` n `6`; index avg `-0.0927` n `27`; metal avg `-0.3058` n `20`; unknown avg `4.3984` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
