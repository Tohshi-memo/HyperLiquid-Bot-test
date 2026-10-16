# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T00:52:34.001432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.0694` n `236`; crypto_major avg `-0.1538` n `8`; equity avg `0.2504` n `151`; fx avg `-0.0018` n `6`; index avg `0.0389` n `26`; metal avg `0.0231` n `20`; unknown avg `0.5525` n `1136`
- 1h: commodity avg `0.0256` n `13`; crypto_alt avg `0.3099` n `236`; crypto_major avg `0.0621` n `8`; equity avg `0.2724` n `151`; fx avg `0.0615` n `6`; index avg `0.0381` n `26`; metal avg `-0.0275` n `20`; unknown avg `0.7028` n `1128`
- 4h: commodity avg `-0.0555` n `13`; crypto_alt avg `-0.0168` n `236`; crypto_major avg `-0.2089` n `8`; equity avg `-0.4177` n `151`; fx avg `0.0427` n `6`; index avg `-0.081` n `26`; metal avg `-0.1114` n `20`; unknown avg `0.7657` n `1090`
- 24h: commodity avg `-0.1032` n `13`; crypto_alt avg `1.1271` n `236`; crypto_major avg `0.5933` n `8`; equity avg `1.4879` n `151`; fx avg `0.0489` n `6`; index avg `0.2252` n `26`; metal avg `0.2114` n `20`; unknown avg `25.5295` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0879`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0808`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0665`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0594`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
