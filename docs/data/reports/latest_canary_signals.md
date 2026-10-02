# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T04:52:29.286934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0482` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.775` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7717` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0009` n `13`; crypto_alt avg `0.3799` n `234`; crypto_major avg `0.3619` n `8`; equity avg `0.0406` n `142`; fx avg `-0.0146` n `6`; index avg `0.0025` n `26`; metal avg `-0.0152` n `20`; unknown avg `54.4094` n `983`
- 1h: commodity avg `-0.0481` n `13`; crypto_alt avg `1.4125` n `234`; crypto_major avg `1.3967` n `8`; equity avg `0.1734` n `142`; fx avg `-0.0295` n `6`; index avg `0.0201` n `26`; metal avg `0.0721` n `20`; unknown avg `1.0148` n `975`
- 4h: commodity avg `-0.117` n `13`; crypto_alt avg `1.716` n `234`; crypto_major avg `1.9312` n `8`; equity avg `0.1562` n `142`; fx avg `-0.0819` n `6`; index avg `0.033` n `26`; metal avg `0.1595` n `20`; unknown avg `2.184` n `975`
- 24h: commodity avg `0.62` n `13`; crypto_alt avg `0.4583` n `234`; crypto_major avg `1.4264` n `8`; equity avg `0.4132` n `142`; fx avg `-0.2249` n `6`; index avg `0.0242` n `26`; metal avg `-0.1105` n `20`; unknown avg `0.7728` n `838`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
