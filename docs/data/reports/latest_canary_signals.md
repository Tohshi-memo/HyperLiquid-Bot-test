# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T01:07:31.260726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.174` n `234`; crypto_major avg `-0.0817` n `8`; equity avg `-0.1189` n `137`; fx avg `-0.0081` n `6`; index avg `-0.032` n `27`; metal avg `-0.0445` n `20`; unknown avg `0.2267` n `917`
- 1h: commodity avg `-0.0283` n `12`; crypto_alt avg `-0.3526` n `234`; crypto_major avg `0.0038` n `8`; equity avg `-0.0459` n `137`; fx avg `0.0725` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0394` n `20`; unknown avg `0.1039` n `911`
- 4h: commodity avg `-0.0758` n `12`; crypto_alt avg `-0.4259` n `234`; crypto_major avg `-0.0683` n `8`; equity avg `-0.1328` n `137`; fx avg `0.1231` n `6`; index avg `-0.0104` n `27`; metal avg `-0.0678` n `20`; unknown avg `0.3294` n `863`
- 24h: commodity avg `0.352` n `12`; crypto_alt avg `-3.9572` n `234`; crypto_major avg `-3.8364` n `8`; equity avg `-1.5914` n `137`; fx avg `0.3002` n `6`; index avg `-0.1664` n `27`; metal avg `0.1463` n `20`; unknown avg `1.2513` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
