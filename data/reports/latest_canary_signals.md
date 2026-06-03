# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T21:52:32.282908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `2.1518` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7676` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.6089` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.6634` n `228`; crypto_major avg `0.5095` n `8`; equity avg `0.3542` n `73`; fx avg `0.0102` n `6`; index avg `0.0482` n `23`; metal avg `0.0467` n `18`; unknown avg `0.145` n `419`
- 1h: commodity avg `0.1308` n `12`; crypto_alt avg `2.1475` n `228`; crypto_major avg `1.8481` n `8`; equity avg `-0.3037` n `73`; fx avg `-0.0307` n `6`; index avg `-0.1592` n `23`; metal avg `0.2392` n `18`; unknown avg `1.1967` n `419`
- 4h: commodity avg `0.2309` n `12`; crypto_alt avg `0.446` n `228`; crypto_major avg `0.2551` n `8`; equity avg `-1.5125` n `73`; fx avg `-0.0077` n `6`; index avg `-0.4581` n `23`; metal avg `-0.2435` n `18`; unknown avg `-0.2567` n `419`
- 24h: commodity avg `1.2099` n `12`; crypto_alt avg `1.4826` n `228`; crypto_major avg `-0.988` n `8`; equity avg `-3.4479` n `72`; fx avg `0.0471` n `6`; index avg `-0.8814` n `23`; metal avg `-2.1692` n `18`; unknown avg `0.2221` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
