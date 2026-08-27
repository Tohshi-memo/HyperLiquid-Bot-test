# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T21:22:25.300098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.0195` n `231`; crypto_major avg `-0.0871` n `8`; equity avg `-0.1012` n `127`; fx avg `-0.0032` n `6`; index avg `-0.0073` n `26`; metal avg `0.0007` n `20`; unknown avg `0.0236` n `792`
- 1h: commodity avg `-0.022` n `12`; crypto_alt avg `0.0724` n `231`; crypto_major avg `-0.2006` n `8`; equity avg `-0.1915` n `127`; fx avg `-0.0128` n `6`; index avg `-0.007` n `26`; metal avg `-0.0282` n `20`; unknown avg `-0.0245` n `792`
- 4h: commodity avg `0.0` n `12`; crypto_alt avg `-0.7082` n `231`; crypto_major avg `-0.6866` n `8`; equity avg `-0.1274` n `127`; fx avg `0.0111` n `6`; index avg `-0.028` n `26`; metal avg `0.0161` n `20`; unknown avg `0.252` n `792`
- 24h: commodity avg `0.3262` n `12`; crypto_alt avg `2.297` n `231`; crypto_major avg `3.2283` n `8`; equity avg `0.2342` n `127`; fx avg `-0.0324` n `6`; index avg `0.0212` n `26`; metal avg `0.2116` n `20`; unknown avg `0.9476` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
