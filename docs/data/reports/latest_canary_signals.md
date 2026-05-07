# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T17:52:17.220870+00:00`
- Correlation status: `ready`
- Asset price records: `571`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6347` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0615` n `12`; crypto_alt avg `0.0786` n `228`; crypto_major avg `0.0069` n `8`; equity avg `-0.1224` n `65`; fx avg `0.0144` n `5`; index avg `-0.1479` n `23`; metal avg `-0.0651` n `18`; unknown avg `0.1067` n `365`
- 1h: commodity avg `0.1886` n `12`; crypto_alt avg `0.1229` n `228`; crypto_major avg `-0.0222` n `8`; equity avg `-0.4068` n `65`; fx avg `-0.0081` n `5`; index avg `-0.3009` n `23`; metal avg `-0.3452` n `18`; unknown avg `0.0955` n `365`
- 4h: commodity avg `1.953` n `12`; crypto_alt avg `-0.0953` n `228`; crypto_major avg `-0.6817` n `8`; equity avg `-1.314` n `65`; fx avg `0.0563` n `5`; index avg `-0.6785` n `23`; metal avg `-1.1889` n `18`; unknown avg `-0.2642` n `365`
- 24h: commodity avg `0.5995` n `12`; crypto_alt avg `0.6676` n `228`; crypto_major avg `-1.8386` n `8`; equity avg `-0.874` n `65`; fx avg `0.1755` n `5`; index avg `-0.6587` n `23`; metal avg `0.5526` n `18`; unknown avg `-0.0406` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1362`, n `567`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `567`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `567`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `567`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0999`, n `563`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0945`, n `563`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `563`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `563`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0891`, n `563`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0772`, n `563`, weak_sample_signal
