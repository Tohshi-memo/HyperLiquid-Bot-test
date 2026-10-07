# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T09:07:28.116137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0694` n `13`; crypto_alt avg `-0.2319` n `235`; crypto_major avg `-0.1466` n `8`; equity avg `-0.1954` n `150`; fx avg `0.0099` n `6`; index avg `-0.0271` n `26`; metal avg `-0.085` n `20`; unknown avg `0.2022` n `1074`
- 1h: commodity avg `-0.0422` n `13`; crypto_alt avg `-0.6063` n `235`; crypto_major avg `-0.3448` n `8`; equity avg `-0.317` n `150`; fx avg `0.0487` n `6`; index avg `-0.0314` n `26`; metal avg `-0.1882` n `20`; unknown avg `0.0217` n `1074`
- 4h: commodity avg `0.0896` n `13`; crypto_alt avg `-0.2085` n `235`; crypto_major avg `-0.0304` n `8`; equity avg `-0.5543` n `150`; fx avg `-0.0798` n `6`; index avg `-0.0884` n `26`; metal avg `-0.2814` n `20`; unknown avg `0.3048` n `1036`
- 24h: commodity avg `0.9834` n `13`; crypto_alt avg `-3.9829` n `235`; crypto_major avg `-2.6134` n `8`; equity avg `-0.8228` n `149`; fx avg `-0.0653` n `6`; index avg `-0.1773` n `26`; metal avg `-0.4428` n `20`; unknown avg `815.1005` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
