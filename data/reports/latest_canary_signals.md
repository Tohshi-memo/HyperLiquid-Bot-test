# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T03:37:30.752698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `0.2399` n `231`; crypto_major avg `0.1177` n `8`; equity avg `-0.0283` n `128`; fx avg `-0.011` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0831` n `20`; unknown avg `0.0179` n `793`
- 1h: commodity avg `-0.0629` n `12`; crypto_alt avg `0.424` n `231`; crypto_major avg `0.0804` n `8`; equity avg `0.184` n `128`; fx avg `-0.0054` n `6`; index avg `0.0602` n `26`; metal avg `0.0683` n `20`; unknown avg `0.0071` n `791`
- 4h: commodity avg `0.1063` n `12`; crypto_alt avg `1.0809` n `231`; crypto_major avg `0.1593` n `8`; equity avg `-0.263` n `128`; fx avg `-0.0689` n `6`; index avg `-0.0337` n `26`; metal avg `-0.2979` n `20`; unknown avg `0.0249` n `779`
- 24h: commodity avg `0.3916` n `12`; crypto_alt avg `-0.2736` n `231`; crypto_major avg `-1.9734` n `8`; equity avg `-1.1213` n `128`; fx avg `-0.0482` n `6`; index avg `-0.2193` n `26`; metal avg `-0.402` n `20`; unknown avg `-0.5089` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
