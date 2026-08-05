# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T09:22:35.412318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0672` n `12`; crypto_alt avg `0.0886` n `230`; crypto_major avg `0.0652` n `8`; equity avg `-0.0954` n `108`; fx avg `-0.0116` n `6`; index avg `0.0003` n `25`; metal avg `-0.0639` n `20`; unknown avg `0.6905` n `781`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `-0.0104` n `230`; crypto_major avg `0.0108` n `8`; equity avg `-0.061` n `108`; fx avg `-0.0195` n `6`; index avg `0.0002` n `25`; metal avg `-0.0917` n `20`; unknown avg `0.6284` n `781`
- 4h: commodity avg `0.2746` n `12`; crypto_alt avg `-0.0342` n `230`; crypto_major avg `0.0417` n `8`; equity avg `-1.0277` n `108`; fx avg `0.0114` n `6`; index avg `-0.1234` n `25`; metal avg `0.0967` n `20`; unknown avg `0.7715` n `749`
- 24h: commodity avg `-1.3029` n `12`; crypto_alt avg `0.811` n `230`; crypto_major avg `1.1794` n `8`; equity avg `2.8201` n `108`; fx avg `-0.0478` n `6`; index avg `0.6894` n `25`; metal avg `1.1457` n `20`; unknown avg `0.2017` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
