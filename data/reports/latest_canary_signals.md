# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T05:37:34.126632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.0887` n `234`; crypto_major avg `-0.0208` n `8`; equity avg `0.0684` n `137`; fx avg `0.0156` n `6`; index avg `0.0001` n `27`; metal avg `0.0015` n `20`; unknown avg `-0.2654` n `919`
- 1h: commodity avg `0.0361` n `12`; crypto_alt avg `-0.2874` n `234`; crypto_major avg `-0.2078` n `8`; equity avg `0.0067` n `137`; fx avg `0.0275` n `6`; index avg `0.0006` n `27`; metal avg `0.004` n `20`; unknown avg `-0.0411` n `917`
- 4h: commodity avg `-0.1005` n `12`; crypto_alt avg `0.4343` n `234`; crypto_major avg `0.5357` n `8`; equity avg `0.72` n `137`; fx avg `-0.0309` n `6`; index avg `0.0736` n `27`; metal avg `0.287` n `20`; unknown avg `1.7307` n `907`
- 24h: commodity avg `0.1338` n `12`; crypto_alt avg `-2.9435` n `234`; crypto_major avg `-2.8076` n `8`; equity avg `-0.2096` n `137`; fx avg `0.1931` n `6`; index avg `0.0453` n `27`; metal avg `0.4419` n `20`; unknown avg `18796.2061` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
