# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T21:52:28.384167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `13`; crypto_alt avg `-0.2865` n `239`; crypto_major avg `-0.361` n `8`; equity avg `-0.3167` n `158`; fx avg `0.0148` n `6`; index avg `-0.0259` n `27`; metal avg `-0.0261` n `20`; unknown avg `0.4117` n `1256`
- 1h: commodity avg `0.0539` n `13`; crypto_alt avg `-0.7828` n `239`; crypto_major avg `-0.7725` n `8`; equity avg `-0.5703` n `158`; fx avg `-0.0045` n `6`; index avg `-0.1799` n `27`; metal avg `-0.1547` n `20`; unknown avg `10.77` n `1242`
- 4h: commodity avg `0.1605` n `13`; crypto_alt avg `0.776` n `239`; crypto_major avg `-0.1487` n `8`; equity avg `-0.1237` n `158`; fx avg `-0.0255` n `6`; index avg `-0.2577` n `27`; metal avg `-0.2059` n `20`; unknown avg `3.289` n `1194`
- 24h: commodity avg `0.9481` n `13`; crypto_alt avg `-4.6443` n `239`; crypto_major avg `-5.0886` n `8`; equity avg `-8.4039` n `158`; fx avg `0.0793` n `6`; index avg `-1.3215` n `27`; metal avg `0.047` n `20`; unknown avg `227.9804` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
