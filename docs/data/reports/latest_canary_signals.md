# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T22:52:33.382033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `13`; crypto_alt avg `-0.038` n `235`; crypto_major avg `-0.0162` n `8`; equity avg `-0.0499` n `150`; fx avg `0.0016` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0089` n `20`; unknown avg `0.212` n `1076`
- 1h: commodity avg `-0.011` n `13`; crypto_alt avg `0.0122` n `235`; crypto_major avg `0.0302` n `8`; equity avg `-0.0321` n `150`; fx avg `-0.0036` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0307` n `20`; unknown avg `-0.019` n `1066`
- 4h: commodity avg `0.0926` n `13`; crypto_alt avg `-0.5` n `235`; crypto_major avg `-0.2226` n `8`; equity avg `-0.1012` n `150`; fx avg `-0.004` n `6`; index avg `-0.0227` n `26`; metal avg `-0.0717` n `20`; unknown avg `0.3504` n `990`
- 24h: commodity avg `0.2965` n `13`; crypto_alt avg `-1.672` n `235`; crypto_major avg `-1.0811` n `8`; equity avg `0.3374` n `149`; fx avg `0.0852` n `6`; index avg `-0.0092` n `26`; metal avg `0.0002` n `20`; unknown avg `871.5509` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
