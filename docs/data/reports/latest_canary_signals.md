# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T00:52:30.055516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0382` n `12`; crypto_alt avg `-0.124` n `234`; crypto_major avg `-0.0718` n `8`; equity avg `-0.0526` n `137`; fx avg `0.0255` n `6`; index avg `-0.0058` n `27`; metal avg `0.0352` n `20`; unknown avg `-0.1434` n `919`
- 1h: commodity avg `-0.0724` n `12`; crypto_alt avg `-0.1118` n `234`; crypto_major avg `0.1029` n `8`; equity avg `0.0627` n `137`; fx avg `0.0786` n `6`; index avg `0.012` n `27`; metal avg `0.0045` n `20`; unknown avg `0.1148` n `911`
- 4h: commodity avg `-0.0504` n `12`; crypto_alt avg `-0.4` n `234`; crypto_major avg `-0.1588` n `8`; equity avg `-0.0521` n `137`; fx avg `0.1205` n `6`; index avg `0.0245` n `27`; metal avg `-0.0097` n `20`; unknown avg `0.3053` n `861`
- 24h: commodity avg `0.3349` n `12`; crypto_alt avg `-3.9084` n `234`; crypto_major avg `-3.8699` n `8`; equity avg `-1.503` n `137`; fx avg `0.3151` n `6`; index avg `-0.1202` n `27`; metal avg `0.2283` n `20`; unknown avg `0.6048` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
