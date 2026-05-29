# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T17:52:22.953387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6017` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1431` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.3905` n `228`; crypto_major avg `-0.3568` n `8`; equity avg `-0.1989` n `69`; fx avg `-0.0044` n `6`; index avg `-0.0986` n `23`; metal avg `-0.0792` n `18`; unknown avg `0.8412` n `419`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.1179` n `228`; crypto_major avg `-0.1646` n `8`; equity avg `0.017` n `69`; fx avg `-0.0079` n `6`; index avg `0.0381` n `23`; metal avg `-0.1898` n `18`; unknown avg `0.9146` n `419`
- 4h: commodity avg `-0.616` n `12`; crypto_alt avg `2.2212` n `228`; crypto_major avg `1.9857` n `8`; equity avg `0.6403` n `69`; fx avg `0.0713` n `6`; index avg `-0.0691` n `23`; metal avg `-0.1574` n `18`; unknown avg `0.8659` n `417`
- 24h: commodity avg `-0.6724` n `12`; crypto_alt avg `1.4139` n `228`; crypto_major avg `1.789` n `8`; equity avg `1.6936` n `69`; fx avg `0.2002` n `6`; index avg `-0.118` n `23`; metal avg `-0.0852` n `18`; unknown avg `1.9779` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
