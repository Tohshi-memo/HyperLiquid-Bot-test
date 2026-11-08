# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T22:52:28.083426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0352` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.7909` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.7077` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5858` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2144` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0646` n `13`; crypto_alt avg `0.4201` n `239`; crypto_major avg `0.3897` n `8`; equity avg `0.093` n `158`; fx avg `-0.0085` n `6`; index avg `0.0021` n `27`; metal avg `0.018` n `20`; unknown avg `0.0766` n `1254`
- 1h: commodity avg `0.2036` n `13`; crypto_alt avg `-0.8615` n `239`; crypto_major avg `-1.2746` n `8`; equity avg `-0.3885` n `158`; fx avg `0.0044` n `6`; index avg `-0.0602` n `27`; metal avg `-0.0606` n `20`; unknown avg `-0.4721` n `1228`
- 4h: commodity avg `0.1505` n `13`; crypto_alt avg `-2.4374` n `239`; crypto_major avg `-2.8847` n `8`; equity avg `-1.2989` n `158`; fx avg `-0.0285` n `6`; index avg `-0.177` n `27`; metal avg `-0.0938` n `20`; unknown avg `0.9716` n `1182`
- 24h: commodity avg `0.0166` n `13`; crypto_alt avg `-3.408` n `239`; crypto_major avg `-2.7851` n `8`; equity avg `-0.7427` n `158`; fx avg `0.0269` n `6`; index avg `-0.1486` n `27`; metal avg `-0.1155` n `20`; unknown avg `-0.8057` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
