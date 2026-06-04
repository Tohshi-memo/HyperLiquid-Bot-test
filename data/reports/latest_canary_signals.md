# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T11:07:24.571672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.9167` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.6701` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0391` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1695` n `12`; crypto_alt avg `0.0269` n `228`; crypto_major avg `0.202` n `8`; equity avg `0.191` n `73`; fx avg `0.0005` n `6`; index avg `0.0426` n `23`; metal avg `0.1118` n `18`; unknown avg `-0.001` n `424`
- 1h: commodity avg `0.0615` n `12`; crypto_alt avg `-0.4605` n `228`; crypto_major avg `-0.7063` n `8`; equity avg `-0.422` n `73`; fx avg `-0.0051` n `6`; index avg `-0.1278` n `23`; metal avg `-0.039` n `18`; unknown avg `1.0194` n `424`
- 4h: commodity avg `0.0643` n `12`; crypto_alt avg `-3.0157` n `228`; crypto_major avg `-2.6058` n `8`; equity avg `-1.4097` n `73`; fx avg `0.0884` n `6`; index avg `-0.5667` n `23`; metal avg `0.3109` n `18`; unknown avg `0.1823` n `424`
- 24h: commodity avg `-0.7949` n `12`; crypto_alt avg `-8.7268` n `228`; crypto_major avg `-7.4049` n `8`; equity avg `-4.8113` n `73`; fx avg `0.0706` n `6`; index avg `-1.5836` n `23`; metal avg `-1.0068` n `18`; unknown avg `-0.6448` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
