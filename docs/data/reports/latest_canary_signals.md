# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T06:37:29.255999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `-0.1958` n `234`; crypto_major avg `-0.2108` n `8`; equity avg `-0.0228` n `137`; fx avg `-0.0102` n `6`; index avg `-0.0037` n `27`; metal avg `0.01` n `20`; unknown avg `1.4848` n `919`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.3244` n `234`; crypto_major avg `-0.2859` n `8`; equity avg `0.1173` n `137`; fx avg `-0.02` n `6`; index avg `0.0598` n `27`; metal avg `-0.0153` n `20`; unknown avg `7.1408` n `889`
- 4h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.2728` n `234`; crypto_major avg `-0.3909` n `8`; equity avg `0.5372` n `137`; fx avg `0.0033` n `6`; index avg `0.0979` n `27`; metal avg `0.0855` n `20`; unknown avg `1.1392` n `877`
- 24h: commodity avg `0.1358` n `12`; crypto_alt avg `-3.3789` n `234`; crypto_major avg `-3.2038` n `8`; equity avg `-0.1297` n `137`; fx avg `0.1651` n `6`; index avg `0.1026` n `27`; metal avg `0.46` n `20`; unknown avg `18940.4076` n `796`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
