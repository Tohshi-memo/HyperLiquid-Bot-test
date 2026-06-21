# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T23:52:30.675358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3882` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `0.1102` n `228`; crypto_major avg `0.079` n `8`; equity avg `-0.1615` n `78`; fx avg `0.0295` n `6`; index avg `-0.0165` n `23`; metal avg `-0.0819` n `18`; unknown avg `0.741` n `702`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.6259` n `228`; crypto_major avg `-0.6563` n `8`; equity avg `-0.6576` n `78`; fx avg `0.0208` n `6`; index avg `-0.1028` n `23`; metal avg `-0.2161` n `18`; unknown avg `2.6838` n `702`
- 4h: commodity avg `-0.1084` n `12`; crypto_alt avg `-1.8161` n `228`; crypto_major avg `-1.5791` n `8`; equity avg `-0.8988` n `78`; fx avg `-0.0075` n `6`; index avg `-0.1909` n `23`; metal avg `-0.2132` n `18`; unknown avg `0.7135` n `702`
- 24h: commodity avg `0.1533` n `12`; crypto_alt avg `-0.8642` n `228`; crypto_major avg `-1.8006` n `8`; equity avg `-0.7511` n `78`; fx avg `-0.1019` n `6`; index avg `-0.1762` n `23`; metal avg `-0.3286` n `18`; unknown avg `0.7989` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
