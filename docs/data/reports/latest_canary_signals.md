# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T10:52:28.728464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `0.0524` n `235`; crypto_major avg `0.0782` n `8`; equity avg `0.0096` n `150`; fx avg `0.0025` n `6`; index avg `-0.0001` n `26`; metal avg `0.002` n `20`; unknown avg `0.005` n `1117`
- 1h: commodity avg `-0.0244` n `13`; crypto_alt avg `-0.1753` n `235`; crypto_major avg `-0.129` n `8`; equity avg `-0.0107` n `150`; fx avg `0.0115` n `6`; index avg `-0.0014` n `26`; metal avg `0.0007` n `20`; unknown avg `0.0989` n `1115`
- 4h: commodity avg `-0.2787` n `13`; crypto_alt avg `-0.4433` n `235`; crypto_major avg `-0.0759` n `8`; equity avg `-0.0363` n `150`; fx avg `0.0002` n `6`; index avg `-0.0051` n `26`; metal avg `0.005` n `20`; unknown avg `0.2215` n `1099`
- 24h: commodity avg `-0.1776` n `13`; crypto_alt avg `2.0506` n `235`; crypto_major avg `0.4674` n `8`; equity avg `-0.1182` n `150`; fx avg `-0.0059` n `6`; index avg `-0.0017` n `26`; metal avg `0.0969` n `20`; unknown avg `631.9631` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
