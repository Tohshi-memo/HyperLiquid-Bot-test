# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T17:07:38.019840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8584` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5469` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0517` n `13`; crypto_alt avg `-0.2897` n `239`; crypto_major avg `-0.4179` n `8`; equity avg `-0.3996` n `168`; fx avg `-0.0072` n `6`; index avg `-0.0439` n `27`; metal avg `-0.0223` n `20`; unknown avg `0.8767` n `1250`
- 1h: commodity avg `-0.0574` n `13`; crypto_alt avg `0.0068` n `239`; crypto_major avg `-0.152` n `8`; equity avg `0.0234` n `168`; fx avg `-0.033` n `6`; index avg `-0.0108` n `27`; metal avg `0.0657` n `20`; unknown avg `0.6347` n `1246`
- 4h: commodity avg `-0.241` n `13`; crypto_alt avg `-1.5915` n `239`; crypto_major avg `-1.908` n `8`; equity avg `-0.7049` n `168`; fx avg `-0.0743` n `6`; index avg `-0.0496` n `27`; metal avg `-0.3611` n `20`; unknown avg `2.2755` n `1244`
- 24h: commodity avg `-0.3832` n `13`; crypto_alt avg `0.2653` n `239`; crypto_major avg `0.7522` n `8`; equity avg `2.8473` n `168`; fx avg `-0.1521` n `6`; index avg `0.2719` n `27`; metal avg `0.7013` n `20`; unknown avg `250.966` n `1027`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
