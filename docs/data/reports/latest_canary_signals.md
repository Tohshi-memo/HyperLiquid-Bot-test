# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T07:37:28.143187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `-0.1785` n `234`; crypto_major avg `-0.0142` n `8`; equity avg `0.0342` n `141`; fx avg `-0.0071` n `6`; index avg `0.0019` n `26`; metal avg `-0.0188` n `20`; unknown avg `9.7811` n `962`
- 1h: commodity avg `0.0277` n `12`; crypto_alt avg `-0.6723` n `234`; crypto_major avg `-0.0896` n `8`; equity avg `-0.5077` n `141`; fx avg `-0.0268` n `6`; index avg `-0.0024` n `26`; metal avg `-0.176` n `20`; unknown avg `10.1437` n `960`
- 4h: commodity avg `0.0981` n `12`; crypto_alt avg `-1.4815` n `234`; crypto_major avg `-0.8194` n `8`; equity avg `-0.6716` n `141`; fx avg `0.0068` n `6`; index avg `-0.0478` n `26`; metal avg `-0.2619` n `20`; unknown avg `1.5996` n `930`
- 24h: commodity avg `-0.3064` n `12`; crypto_alt avg `-3.8838` n `234`; crypto_major avg `-2.6809` n `8`; equity avg `-2.2942` n `141`; fx avg `0.0611` n `6`; index avg `-0.2282` n `26`; metal avg `-0.9829` n `20`; unknown avg `4.2294` n `815`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
