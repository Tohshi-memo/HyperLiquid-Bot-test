# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T14:07:19.975628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6534` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5806` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.2724` n `12`; crypto_alt avg `0.146` n `228`; crypto_major avg `0.2162` n `8`; equity avg `0.0659` n `67`; fx avg `0.0011` n `6`; index avg `0.0197` n `23`; metal avg `0.0255` n `18`; unknown avg `0.1909` n `418`
- 1h: commodity avg `0.184` n `12`; crypto_alt avg `0.2349` n `228`; crypto_major avg `0.5356` n `8`; equity avg `0.0407` n `67`; fx avg `-0.0189` n `6`; index avg `0.3771` n `23`; metal avg `-0.0098` n `18`; unknown avg `0.4502` n `418`
- 4h: commodity avg `0.2494` n `12`; crypto_alt avg `1.6609` n `228`; crypto_major avg `1.8786` n `8`; equity avg `0.2252` n `67`; fx avg `-0.0493` n `6`; index avg `0.5484` n `23`; metal avg `0.298` n `18`; unknown avg `1.0588` n `417`
- 24h: commodity avg `0.6814` n `12`; crypto_alt avg `0.3241` n `228`; crypto_major avg `-0.054` n `8`; equity avg `-0.4043` n `67`; fx avg `-0.1483` n `6`; index avg `0.4262` n `23`; metal avg `-0.714` n `18`; unknown avg `-0.3019` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
