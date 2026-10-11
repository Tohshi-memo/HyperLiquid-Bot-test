# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T01:49:22.759884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `0.1822` n `235`; crypto_major avg `0.0023` n `8`; equity avg `0.0139` n `150`; fx avg `0.005` n `6`; index avg `0.0008` n `26`; metal avg `0.0017` n `20`; unknown avg `1.6282` n `1117`
- 1h: commodity avg `-0.0267` n `13`; crypto_alt avg `0.736` n `235`; crypto_major avg `0.2449` n `8`; equity avg `0.0212` n `150`; fx avg `0.0037` n `6`; index avg `-0.0049` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.1302` n `1115`
- 4h: commodity avg `0.0512` n `13`; crypto_alt avg `0.1646` n `235`; crypto_major avg `-0.0638` n `8`; equity avg `-0.0196` n `150`; fx avg `0.0072` n `6`; index avg `-0.0008` n `26`; metal avg `0.0068` n `20`; unknown avg `3.5023` n `1101`
- 24h: commodity avg `0.0515` n `13`; crypto_alt avg `1.6429` n `235`; crypto_major avg `0.3118` n `8`; equity avg `0.0861` n `150`; fx avg `-0.0046` n `6`; index avg `-0.017` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.3165` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
