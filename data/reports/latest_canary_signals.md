# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T23:22:17.894143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.153` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `-0.0588` n `228`; crypto_major avg `0.0216` n `8`; equity avg `0.0323` n `67`; fx avg `0.0074` n `6`; index avg `0.0628` n `23`; metal avg `0.0189` n `18`; unknown avg `-0.0268` n `396`
- 1h: commodity avg `0.0994` n `12`; crypto_alt avg `-0.3952` n `228`; crypto_major avg `0.0145` n `8`; equity avg `0.062` n `67`; fx avg `0.0067` n `6`; index avg `0.0408` n `23`; metal avg `0.162` n `18`; unknown avg `-0.2973` n `396`
- 4h: commodity avg `-1.4201` n `12`; crypto_alt avg `0.5642` n `228`; crypto_major avg `0.7329` n `8`; equity avg `0.7692` n `67`; fx avg `0.081` n `6`; index avg `0.3248` n `23`; metal avg `0.5162` n `18`; unknown avg `0.1082` n `396`
- 24h: commodity avg `-2.7477` n `12`; crypto_alt avg `1.7492` n `228`; crypto_major avg `1.5703` n `8`; equity avg `1.6116` n `67`; fx avg `0.0585` n `6`; index avg `0.7826` n `23`; metal avg `0.734` n `18`; unknown avg `0.01` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
