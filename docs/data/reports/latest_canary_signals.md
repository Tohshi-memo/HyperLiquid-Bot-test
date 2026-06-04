# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T08:07:29.139003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.019` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9539` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.9284` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.6835` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.3224` n `228`; crypto_major avg `-0.2271` n `8`; equity avg `-0.0727` n `73`; fx avg `0.038` n `6`; index avg `-0.044` n `23`; metal avg `0.1173` n `18`; unknown avg `-0.1044` n `424`
- 1h: commodity avg `0.1334` n `12`; crypto_alt avg `-0.8827` n `228`; crypto_major avg `-0.6187` n `8`; equity avg `-0.2133` n `73`; fx avg `0.0797` n `6`; index avg `-0.0696` n `23`; metal avg `0.1011` n `18`; unknown avg `-0.2852` n `424`
- 4h: commodity avg `0.0661` n `12`; crypto_alt avg `-3.1144` n `228`; crypto_major avg `-2.9529` n `8`; equity avg `-0.2694` n `73`; fx avg `0.1176` n `6`; index avg `0.001` n `23`; metal avg `-0.0245` n `18`; unknown avg `-1.2131` n `404`
- 24h: commodity avg `-0.4517` n `12`; crypto_alt avg `-5.9808` n `228`; crypto_major avg `-5.3885` n `8`; equity avg `-3.7067` n `73`; fx avg `0.0718` n `6`; index avg `-1.0897` n `23`; metal avg `-0.9677` n `18`; unknown avg `-1.0902` n `403`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
