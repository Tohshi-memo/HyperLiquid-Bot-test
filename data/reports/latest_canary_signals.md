# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T10:37:25.317721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.1894` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.1289` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4099` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5852` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0941` n `12`; crypto_alt avg `-0.0194` n `228`; crypto_major avg `0.0112` n `8`; equity avg `0.0085` n `73`; fx avg `0.0037` n `6`; index avg `-0.061` n `23`; metal avg `0.0059` n `18`; unknown avg `-0.172` n `424`
- 1h: commodity avg `0.211` n `12`; crypto_alt avg `0.5172` n `228`; crypto_major avg `0.2741` n `8`; equity avg `-0.231` n `73`; fx avg `-0.0014` n `6`; index avg `-0.1093` n `23`; metal avg `-0.0312` n `18`; unknown avg `0.0174` n `424`
- 4h: commodity avg `0.196` n `12`; crypto_alt avg `-3.45` n `228`; crypto_major avg `-2.9329` n `8`; equity avg `-1.3477` n `73`; fx avg `0.1083` n `6`; index avg `-0.523` n `23`; metal avg `0.2565` n `18`; unknown avg `-1.0482` n `424`
- 24h: commodity avg `-0.8104` n `12`; crypto_alt avg `-7.7631` n `228`; crypto_major avg `-6.5493` n `8`; equity avg `-4.5421` n `73`; fx avg `0.067` n `6`; index avg `-1.5388` n `23`; metal avg `-0.9928` n `18`; unknown avg `-1.2183` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
