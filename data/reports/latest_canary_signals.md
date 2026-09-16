# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T12:37:28.423647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.042` n `12`; crypto_alt avg `-0.081` n `234`; crypto_major avg `-0.2222` n `8`; equity avg `-0.1161` n `137`; fx avg `0.007` n `6`; index avg `-0.0206` n `27`; metal avg `-0.0134` n `20`; unknown avg `-0.0844` n `913`
- 1h: commodity avg `0.1088` n `12`; crypto_alt avg `-0.2572` n `234`; crypto_major avg `-0.3735` n `8`; equity avg `-0.0114` n `137`; fx avg `0.0229` n `6`; index avg `0.0158` n `27`; metal avg `-0.1007` n `20`; unknown avg `0.5965` n `911`
- 4h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.6093` n `234`; crypto_major avg `0.6498` n `8`; equity avg `0.3504` n `137`; fx avg `-0.0336` n `6`; index avg `0.0759` n `27`; metal avg `0.0845` n `20`; unknown avg `0.3977` n `911`
- 24h: commodity avg `0.1827` n `12`; crypto_alt avg `-2.943` n `234`; crypto_major avg `-2.7504` n `8`; equity avg `-0.0637` n `137`; fx avg `0.0735` n `6`; index avg `0.0756` n `27`; metal avg `0.3924` n `20`; unknown avg `18892.8594` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
