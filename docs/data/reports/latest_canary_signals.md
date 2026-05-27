# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T23:37:15.541701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7483` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7401` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5333` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.1448` n `228`; crypto_major avg `-0.2231` n `8`; equity avg `-0.1407` n `67`; fx avg `-0.0046` n `6`; index avg `-0.059` n `23`; metal avg `0.0132` n `18`; unknown avg `-0.2926` n `419`
- 1h: commodity avg `0.084` n `12`; crypto_alt avg `-0.622` n `228`; crypto_major avg `-0.7948` n `8`; equity avg `-0.109` n `67`; fx avg `-0.0087` n `6`; index avg `-0.0849` n `23`; metal avg `-0.1357` n `18`; unknown avg `-0.1723` n `419`
- 4h: commodity avg `0.1772` n `12`; crypto_alt avg `-2.4714` n `228`; crypto_major avg `-1.7865` n `8`; equity avg `-0.2532` n `67`; fx avg `-0.0303` n `6`; index avg `-0.0464` n `23`; metal avg `-0.0382` n `18`; unknown avg `0.0798` n `419`
- 24h: commodity avg `-0.9724` n `12`; crypto_alt avg `-2.5384` n `228`; crypto_major avg `-1.805` n `8`; equity avg `-0.4232` n `67`; fx avg `-0.1072` n `6`; index avg `-0.6017` n `23`; metal avg `-1.5305` n `18`; unknown avg `-0.544` n `400`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
