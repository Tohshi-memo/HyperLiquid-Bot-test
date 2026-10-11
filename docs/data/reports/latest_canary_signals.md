# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T12:37:29.238569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `0.0645` n `235`; crypto_major avg `-0.0819` n `8`; equity avg `-0.0258` n `150`; fx avg `-0.0078` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.2142` n `1117`
- 1h: commodity avg `-0.0206` n `13`; crypto_alt avg `0.2741` n `235`; crypto_major avg `0.0774` n `8`; equity avg `0.0802` n `150`; fx avg `-0.0171` n `6`; index avg `0.0039` n `26`; metal avg `0.0032` n `20`; unknown avg `0.5099` n `1109`
- 4h: commodity avg `-0.0239` n `13`; crypto_alt avg `-0.1555` n `235`; crypto_major avg `0.0852` n `8`; equity avg `0.1184` n `150`; fx avg `0.0123` n `6`; index avg `0.0042` n `26`; metal avg `0.0006` n `20`; unknown avg `0.5808` n `1109`
- 24h: commodity avg `0.3592` n `13`; crypto_alt avg `1.2055` n `235`; crypto_major avg `0.0922` n `8`; equity avg `0.1503` n `150`; fx avg `0.0046` n `6`; index avg `-0.001` n `26`; metal avg `0.0114` n `20`; unknown avg `0.6495` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
