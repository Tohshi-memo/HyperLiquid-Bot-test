# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T04:37:26.264979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.0113` n `232`; crypto_major avg `-0.0775` n `8`; equity avg `-0.0552` n `133`; fx avg `-0.0149` n `6`; index avg `-0.0131` n `26`; metal avg `0.0286` n `20`; unknown avg `1.529` n `792`
- 1h: commodity avg `-0.0427` n `12`; crypto_alt avg `0.1527` n `232`; crypto_major avg `-0.1048` n `8`; equity avg `0.0142` n `133`; fx avg `-0.0428` n `6`; index avg `-0.0098` n `26`; metal avg `0.0453` n `20`; unknown avg `203.8402` n `790`
- 4h: commodity avg `-0.022` n `12`; crypto_alt avg `0.9558` n `232`; crypto_major avg `0.7273` n `8`; equity avg `0.3409` n `133`; fx avg `-0.143` n `6`; index avg `0.0507` n `26`; metal avg `0.2848` n `20`; unknown avg `204.1572` n `790`
- 24h: commodity avg `0.1918` n `12`; crypto_alt avg `0.3611` n `232`; crypto_major avg `0.2042` n `8`; equity avg `1.6679` n `133`; fx avg `-0.399` n `6`; index avg `0.2126` n `26`; metal avg `0.9437` n `20`; unknown avg `2.8079` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.043`, n `668`, weak_sample_signal
