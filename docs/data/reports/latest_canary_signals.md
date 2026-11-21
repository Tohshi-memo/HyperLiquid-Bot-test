# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T09:37:29.852705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7861` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6107` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9746` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `0.133` n `239`; crypto_major avg `0.1265` n `8`; equity avg `0.1364` n `166`; fx avg `-0.0454` n `6`; index avg `0.0151` n `27`; metal avg `0.0097` n `20`; unknown avg `317.1173` n `1262`
- 1h: commodity avg `0.0018` n `13`; crypto_alt avg `1.1733` n `239`; crypto_major avg `1.1433` n `8`; equity avg `0.145` n `166`; fx avg `0.0067` n `6`; index avg `0.0202` n `27`; metal avg `0.0467` n `20`; unknown avg `330.1454` n `1258`
- 4h: commodity avg `-0.0314` n `13`; crypto_alt avg `1.7549` n `239`; crypto_major avg `2.7547` n `8`; equity avg `0.7801` n `166`; fx avg `-0.0792` n `6`; index avg `0.0748` n `27`; metal avg `0.144` n `20`; unknown avg `207.4265` n `1208`
- 24h: commodity avg `0.8139` n `13`; crypto_alt avg `-5.524` n `239`; crypto_major avg `-6.1469` n `8`; equity avg `-4.3059` n `166`; fx avg `-0.1155` n `6`; index avg `-0.4958` n `27`; metal avg `-0.3625` n `20`; unknown avg `183.2567` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
